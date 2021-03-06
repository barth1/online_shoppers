from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


from App_Order.models import Cart, Order
from App_Shop.models import Product


from django.contrib import messages





@login_required
def add_to_cart(request,pk):
    item= get_object_or_404(Product, pk=pk)
    # it get all the objects in the Product class but returns 404 if there no objects
    order_item= Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    #the get_or_create built in function checks if the products is already added to the cart or not if now then it create a products
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    #this is for the incomplete order i.e the order is alreaady added to cart but not the order is not made

    if order_qs.exists():
        order= order_qs[0]
        if  order. orderitem.filter(item=item).exists(): 
            order_item[0].quantity +=1
            order_item[0].save()
            messages.info(request, "This item quantiy was updated")
            return redirect("App_Shop:home")
        else:
            order. orderitem.add(order_item[0])
            messages.info(request, "This item is added to your cart")
            return redirect("App_Shop:home")
    else:
        order=Order(user=request.user)
        order.save()
        order. orderitem.add(order_item[0])
        messages.info(request, "This item is added to your cart")
        return redirect("App_Shop:home")

    # this function is to check if a  particular product exists in the cart and if yes then it should just increase the quantity or add to cart



@login_required
def cart_view(request):
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders=Order.objects.filter(user=request.user, ordered=False)
    if carts.exists and orders.exists():
        order=orders[0]
        return render (request, 'App_Order/cart.html', context={'carts':carts, 'order':order})
    else:
        messages.warning(request, "You don't have any item in your cart")
        return redirect("App_Shop:home")

@login_required
def remove_from_cart(request, pk):
    item= get_object_or_404(Product, pk=pk)
    order_qs=Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if  order.orderitem.filter(item=item).exists():
            order_item=Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            order.orderitem.remove(order_item)
            order_item.delete()
            messages.warning(request, "This itme was removed from your cart")
            return redirect("App_Order:cart")
        else:
            messages.info(request, "This item wasn't in your cart")
            return redirect("App_Shop:home")
    else:
        messages.info(request, "you don't have any active order")
        return redirect ("App_shop:home")


@login_required
def increase_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs=Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        if order.orderitem.filter(item=item).exists():
            order_item =Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity +=1
                order_item.save()
                messages.info(request, f"{item.name} quantity has been updated")
                return redirect("App_Order:cart")
            else:
                messages.info(request, f"{item.name} is not in your cart")
                return redirect("App_Shop:home")
        else:
            messages.info(request, "Your don't have an active order")
            return redirect("App_Shop:home")

@login_required
def decrease_cart(request,pk):
    item =get_object_or_404(Product, pk=pk)
    order_qs= Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        if order.orderitem.filter(item=item).exists():
            order_item=Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, f"{item.name} quantity has been updated")
                return redirect("App_Order:cart")
            else:
                order.orderitem.remove(order_item)
                order_item.delete()
                messages.warning(request, f"{item.name} has been removed from your cart")
                return redirect("App_Order:cart")
        else:
            messages.info(request, "Your don't have an active order")
            return redirect("App_Shop:home")


