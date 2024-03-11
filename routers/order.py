from fastapi import APIRouter, Depends, HTTPException

from schema.order import Order, OrderCreate, orders, OrderStatus
from services.order import order_service

order_router = APIRouter()

# list all order
# create an order
# check out an order 

@order_router.get('/', status_code=200)
def list_orders():
    response = order_service.order_parser(orders)
    return {'message': 'success', 'data': response}

@order_router.post('/', status_code=201, response_model=Order)
def create_order(payload: OrderCreate = Depends(order_service.check_availability)) -> Order:
    customer_id: int = payload.customer_id
    product_ids: list[int] = payload.items
    # get curr order id
    order_id = len(orders) + 1
    new_order = Order(
        id=order_id,
        customer_id=customer_id,
        items=product_ids,
        status=OrderStatus.pending 
    )
    orders.append(new_order)
    return {'message': 'Order created successfully', 'data': new_order}


@order_router.put('/{order_id}/checkout', status_code=200, response_model=Order)
def checkout_order(order_id: int):
    # Find the order with the given order_id
    for order in orders:
        if order.id == order_id:
            # Check if the order is already completed
            if order.status == OrderStatus.completed:
                raise HTTPException(status_code=400, detail="Order is already completed")
            # Update the status to 'completed'
            order.status = OrderStatus.completed
            return order
    # If the order_id is not found, raise HTTPException
    raise HTTPException(status_code=404, detail="Order not found")

