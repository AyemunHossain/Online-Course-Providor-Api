
# class OrderViewSet(viewsets.ModelViewSet):

#     queryset = Order.objects.all()
#     #authentication_classes = [TokenAuthentication]
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [ permissions.IsAuthenticated ]
#     #permission_classes = [permissions.AllowAny]
#     serializer_class = OrderSerializer
#     #parser_classes = (MultiPartParser, FormParser,)

#     def get_object(self, queryset=None, **kwargs):
#         pk = self.kwargs.get('pk')
#         try:
#             data = Order.objects.filter(pk=pk, ordered=False)
#             return data
#         except:
#             return None

#     def get_queryset(self):
#         return Order.objects.all()

#     def create(self, request, *args, **kwargs):

#         try:
#             cartItem = OrderCourse.objects.filter(
#                 user=self.request.user.id, ordered=False)

#             data = {
#             'user':request.user.id,
#             'items': [obj.id for obj in cartItem],}
#         except:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#         try:
#             serializer = self.get_serializer(data=data)
#             serializer.is_valid(raise_exception=True)
#         except:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
