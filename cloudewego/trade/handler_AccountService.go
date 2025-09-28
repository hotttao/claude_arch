package main

import (
	account "cloudewego/kitex_gen/trade/account"
	"context"
)

// AccountServiceImpl implements the last service interface defined in the IDL.
type AccountServiceImpl struct{}

// QueryPositions implements the AccountServiceImpl interface.
func (s *AccountServiceImpl) QueryPositions(ctx context.Context, req *account.QueryPositionsRequest) (resp *account.QueryPositionsResponse, err error) {
	// TODO: Your code here...
	return
}

// QueryAccount implements the AccountServiceImpl interface.
func (s *AccountServiceImpl) QueryAccount(ctx context.Context, req *account.QueryAccountRequest) (resp *account.QueryAccountResponse, err error) {
	// TODO: Your code here...
	return
}
