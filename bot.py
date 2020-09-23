from stex_client.public import Public

public = Public()
ping = public.ping() #https://apidocs.stex.com/#/Public/get_public_ping

if ping['success']:
    print("Welcome champ :)")

    ################## Your code here ##################
    print(public.currencies_by_id(71))
    print(public.currency_pairs_by_id(80))

else:
    print("Something went wrong :(")


"""
public.currencies() #https://apidocs.stex.com/#/Public/get_public_currencies
public.currencies_by_id(1) #https://apidocs.stex.com/#/Public/get_public_currencies__currencyId_
public.markets() #https://apidocs.stex.com/#/Public/get_public_markets
public.pairs_groups() #https://apidocs.stex.com/#/Public/get_public_pairs_groups
public.currency_pairs_list('BTC') #https://apidocs.stex.com/#/Public/get_public_currency_pairs_list__code_
public.pairs_groups_by_id(1) #https://apidocs.stex.com/#/Public/get_public_currency_pairs_group__currencyPairGroupId_
public.currency_pairs_by_id(1) #https://apidocs.stex.com/#/Public/get_public_currency_pairs__currencyPairId_
public.ticker() #https://apidocs.stex.com/#/Public/get_public_ticker
public.ticker_by_currency_pair_id(1) #https://apidocs.stex.com/#/Public/get_public_ticker__currencyPairId_
public.trades_by_currency_pair_id(1, {'limit': 1}) #https://apidocs.stex.com/#/Public/get_public_trades__currencyPairId_
public.orderbook_by_currency_pair_id(1, {'limit_bids': 1, 'limit_asks': 1}) #https://apidocs.stex.com/#/Public/get_public_orderbook__currencyPairId_
public.chart(1, '1D') #https://apidocs.stex.com/#/Public/get_public_chart__currencyPairId___candlesType_
"""