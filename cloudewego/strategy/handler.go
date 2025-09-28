package main

import (
	strategy "cloudewego/kitex_gen/strategy"
	"context"
)

// StrategyServiceImpl implements the last service interface defined in the IDL.
type StrategyServiceImpl struct{}

// QueryStrategySelected implements the StrategyServiceImpl interface.
func (s *StrategyServiceImpl) QueryStrategySelected(ctx context.Context, req *strategy.QueryStrategySelectedReq) (resp *strategy.QueryStrategySelectedRes, err error) {
	// TODO: Your code here...
	return
}
