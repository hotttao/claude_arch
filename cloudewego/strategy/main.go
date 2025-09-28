package main

import (
	strategy "cloudewego/kitex_gen/strategy/strategyservice"
	"log"
)

func main() {
	svr := strategy.NewServer(new(StrategyServiceImpl))

	err := svr.Run()

	if err != nil {
		log.Println(err.Error())
	}
}
