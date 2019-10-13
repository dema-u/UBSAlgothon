import pandas as pd
import matplotlib.pyplot as plt

TRADING_DAYS_IN_YEAR = 252

def get_cumulative_return(series):
    '''Get percentage return on investment.'''

    roi = ((series[-1]-series[0])/series[0])*100
    return round(roi, 3)


def get_annual_return(series):
    '''Get annual percentage return'''
    total_pnl = series[-1] - series[0]
    annual_return = total_pnl * TRADING_DAYS_IN_YEAR / len(series)
    return round(annual_return, 3)


def get_sharpe_ratio(series, risk_free_rate=0):
    '''Get sharpe ratio'''
    cumulative_return = get_cumulative_return(series)
    return_stddev = ((series/series[0])*100).std()
    sharpe_ratio = (cumulative_return-risk_free_rate)/return_stddev
    return round(sharpe_ratio, 3)


def get_max_draw_down(series):
    '''Get percentage draw-down'''
    draw_down = ((min(series) - max(series))/max(series))*100
    return round(draw_down, 3)


def print_full_statistics(series):
    '''Print all the relevant statistics for this task'''
    print('-'*30)
    print('Total % Return:        ' + str(get_cumulative_return(series)) + '%')
    print('Total % Annual Return: ' + str(get_annual_return(series)) + '%')
    print('Maximum % Drawdown:    ' + str(get_max_draw_down(series)) + '%')
    print('Sharpe Ratio:          ' + str(get_sharpe_ratio(series)))
    print('-' * 30)

    fig, ax = plt.subplots(figsize=(20, 5))

    (series/series[0]).plot(ax=ax)

    ax.set_title('% Returns')
    ax.set_ylabel('Price')
    ax.set_xlabel('Date')
    ax.grid(alpha=0.5)

    return None