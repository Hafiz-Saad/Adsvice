URL = 'https://graph.facebook.com/v17/insights/?cpc=svfd'
def facebook_ecommerce_cold():
    """
    Facebook Ecommerce Cold Campaign
    """
    product_price = 100
    cpa_goal = 10
    CPA = 5
    CPM = 30
    conversion_rate = 1.7
    CTR = 1.6
    CPC = 10
    daily_amount_set = 50
    daily_amount_spent = 40
    purchase = 100
    turn_over = product_price * purchase
    ROAS = turn_over / daily_amount_spent
    # for cold
    if  CPM > 25:
        if  conversion_rate >= 1.5:
            print('The audience is expensive but conversion rate is good')
            print('you should continue and take care of you cpm.')
        else:
            print('The audience is expensive and do not convert better.')
            print('you should stop the campaian.')

    if CTR > 1:
        if CPC > 3:
            print('The audienec is expensive')
            print('you should try new audience.')
        elif CPC < 2:
            print('The CPC is good')

    if CTR > 1.5:
        print('your creatives are good')
    elif CTR < 1.5:
        print('you probably have a problem with your ads creative')


    if conversion_rate < 1:
        print('problem with offer or website page.')
    elif conversion_rate > 1:
        print('your page or offer convert well.')


    if daily_amount_spent < daily_amount_set:
        print('problem of settings.It can be from the audience, the placement...')
    
    elif daily_amount_spent == daily_amount_set or \
        [daily_amount_spent > daily_amount_set and daily_amount_spent < (daily_amount_set + 20)]:
        print('Perfect, the campaign is running,\
             no worries is you spend a little bit more that excepts isn’t normal')
        
    elif daily_amount_spent > (daily_amount_set + 20):
        print('you should stop compaign, something is going wrong.')




def facebook_ecommerce_retargetting():
    """
    Facebook Ecommerce retargetting campain
    """
    product_price = 100
    cpa_goal = 10
    CPA = 5
    CPM = 30
    conversion_rate = 1.7
    CTR = 1.6
    CPC = 10
    daily_amount_set = 50
    daily_amount_spent = 40
    purchase = 100
    turn_over = product_price * purchase
    ROAS = turn_over / daily_amount_spent

    if CPM > 40:
        if conversion_rate >= 1.5:
            print('you should continue and take care of your CPM.')
        else:
            print('stop the campaign')
    
    if CTR > 1:
        if CPC > 3:
            print('you should try new retargeting audience')
        elif CPC < 2:
            print('The CPC is good')

    if CTR > 1.5:
        print('your creatives are good')
    elif CTR < 1.5:
        print('you probably have a problem with your ads creative')

    if conversion_rate < 1:
        print('problem with offer or website page.')
    elif conversion_rate > 1:
        print('your page or offer convert well.')

    if daily_amount_spent < daily_amount_set:
        print('problem of settings.It can be from the audience, the placement...')
    
    elif daily_amount_spent == daily_amount_set or \
        [daily_amount_spent > daily_amount_set and daily_amount_spent < (daily_amount_set + 20)]:
        print('Perfect, the campaign is running,\
             no worries is you spend a little bit more that excepts isn’t normal')
        
    elif daily_amount_spent > (daily_amount_set + 20):
        print('you should stop compaign, something is going wrong.')



def facebook_lead_generation_cold():
    cpl_goal = 10
    CPL = 8
    CPM = 30
    conversion_rate = 1.7
    CTR = 1.6
    CPC = 10
    daily_amount_set = 50
    daily_amount_spent = 40
    leads = 200
    
    if CPM > 25:
        if conversion_rate >= 1.5:
            print('Your audience expensive BUT qualified. You should continue to monitor your CPM')
        else:
            print('stop the campaign')

    if CTR > 1:
        if CPC > 3:
            print('you should try new audience.')
        elif CPC < 2:
            print('The CPC is good')

    
    if CTR > 1.5:
        print('your creatives are good')
    elif CTR < 1.5:
        print('you probably have a problem with your ads creative')

    if conversion_rate < 1:
        print('problem with offer or website page.')
    elif conversion_rate > 1:
        print('your page or offer convert well.')

    if daily_amount_spent < daily_amount_set:
        print('problem of settings.It can be from the audience, the placement...')
    
    elif daily_amount_spent == daily_amount_set or \
        [daily_amount_spent > daily_amount_set and daily_amount_spent < (daily_amount_set + 20)]:
        print('Perfect, the campaign is running,\
             no worries is you spend a little bit more that excepts isn’t normal')
        
    elif daily_amount_spent > (daily_amount_set + 20):
        print('you should stop compaign, something is going wrong.')


facebook_ecommerce_cold()
print("Facebook Retargeting\n\n")
facebook_ecommerce_retargetting()
print("Facebook Lead\n\n")
facebook_lead_generation_cold()

