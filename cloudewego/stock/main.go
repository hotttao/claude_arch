package main

import (
	trade "cloudewego/kitex_gen/stock/trade/stocktradeservice"
	"log"
)

func main() {
	svr := trade.NewServer(new(StockTradeServiceImpl))

	err := svr.Run()

	if err != nil {
		log.Println(err.Error())
	}
}
