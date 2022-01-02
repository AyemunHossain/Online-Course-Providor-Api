from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
import stripe
from django.contrib.auth.decorators import login_required
from .models import Order, Payment
from UserManagement.models import UserAccount as User
import datetime

stripe.api_key = settings.STRIP_KEY
stripe.log = 'info'

class StripeCheckoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': 'price_1KAr1FAz9OavjjPhEHvL2lHl',
                        'quantity': 1,
                    },
                ],
                client_reference_id = request.user.id,
                metadata={
                    'orderRef': request.data.get('orderRef'),
                    }, 
                payment_method_types=['card', ],
                mode='payment',
                success_url=settings.FONTEND_URL +
                '/order-payment-status/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url=settings.FONTEND_URL + '/order-payment-status/?canceled=true',
            )
            return Response(checkout_session.url,status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(
                e,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class StripePaymentStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        
        try:
            already_existed = Payment.objects.get(
                stripe_charge_id=request.data.get('checkoutId'))
            if(already_existed):
                return Response({'status':'used'}, status=status.HTTP_226_IM_USED)
        except:
            pass
        
        
        line_items = []
        paymentObjStatus = False
        try:
            line_items = stripe.checkout.Session.retrieve(
                request.data.get('checkoutId'),
            )
            
            #colecting data and create payment and update orderdetails
            try:
                order_ref = line_items.metadata.orderRef
                user = line_items.client_reference_id
                stripe_charge_id = line_items.id
                amount = line_items.amount_total
                paymentObjStatus = PayementAndOrderUpdate(request, order_ref, user, stripe_charge_id, amount)
            except Exception as e :
                return Response({"error": f"{e}"}, status=status.HTTP_204_NO_CONTENT)
            return Response(line_items, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response([],status=status.HTTP_204_NO_CONTENT)


@login_required()
def PayementAndOrderUpdate(request, order_ref, user, stripe_charge_id, amount):

    order = Order.objects.filter(user=request.user.id, refrence_code=order_ref, ordered=False).last()
    order_items = order.items.all()
    try:
        for item in order_items:
            item.ordered = True

            item.save()
        
        order.ordered = True
        
        try:
            userOj = User.objects.get(id=user)
            payment = Payment.objects.create(
            user=userOj, order_ref=order_ref, stripe_charge_id=stripe_charge_id, amount=amount)
            payment.save()
        except Exception as E:
            return E            
        order.ordered_completion_date = datetime.datetime.now()
        order.payment_status = True
        order.save()
        return True
        
    except Exception as E:
            return E
    