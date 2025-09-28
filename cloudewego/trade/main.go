package main

import (
	serviceAccountService "cloudewego/kitex_gen/trade/account/accountservice"
	server "github.com/cloudwego/kitex/server"
	"log"
)

func main() {
	svr := server.NewServer()
	if err := serviceAccountService.RegisterService(svr, new(AccountServiceImpl)); err != nil {
		panic(err)
	}

	err := svr.Run()

	if err != nil {
		log.Println(err.Error())
	}
}
