package main

import (
	order "cloudewego/kitex_gen/trade/order"
	"context"
)

// OrderServiceImpl implements the last service interface defined in the IDL.
type OrderServiceImpl struct{}

// PlaceOrder implements the OrderServiceImpl interface.
func (s *OrderServiceImpl) PlaceOrder(ctx context.Context, req *order.OrderRequest) (resp *order.OrderResponse, err error) {
	// TODO: Your code here...
	return
}
