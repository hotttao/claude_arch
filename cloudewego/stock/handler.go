package main

import (
	trade "cloudewego/kitex_gen/stock/trade"
	"context"
)

// StockTradeServiceImpl implements the last service interface defined in the IDL.
type StockTradeServiceImpl struct{}

// GetStockTradeData implements the StockTradeServiceImpl interface.
func (s *StockTradeServiceImpl) GetStockTradeData(ctx context.Context, req *trade.GetStockTradeDataReq) (resp *trade.GetStockTradeDataRes, err error) {
	// TODO: Your code here...
	return
}

func (s *StockTradeServiceImpl) StreamTradeData(req *trade.StreamTradeDataReq, stream trade.StockTradeService_StreamTradeDataServer) (err error) {
	println("StreamTradeData called")
	return
}
