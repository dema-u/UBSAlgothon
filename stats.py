import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

TRADING_DAYS_IN_YEAR = 252

def get_cumulative_return(series):
    '''
    Get percentage return on investment.
    '''

    roi = ((series[-1]-series[0])/series[0])*100
    return round(roi, 3)


def get_annualized_return(series):
    '''
    Get annual percentage return
    '''
    annual_return = (series[-1] - series[0]) * TRADING_DAYS_IN_YEAR / len(series) / series[0]
    return round(annual_return*100, 3)


def get_sharpe_ratio(series, risk_free_rate=0):
    '''
    Get sharpe ratio
    '''
    cumulative_return = get_cumulative_return(series)
    return_stddev = ((np.array(series)/series[0])*100).std()
    sharpe_ratio = (cumulative_return-risk_free_rate)/return_stddev
    return round(sharpe_ratio, 3)


def get_max_draw_down(series):
    '''
    Get percentage draw-down
    '''
    draw_down = ((min(series) - max(series))/max(series))*100
    return round(draw_down, 3)


def print_full_statistics(series):
    '''
    Print all the relevant statistics for this task
    '''
    print('-'*30)
    print('Total % Return:        ' + str(get_cumulative_return(series)) + '%')
    print('Total % Annual Return: ' + str(get_annualized_return(series)) + '%')
    print('Maximum % Drawdown:    ' + str(get_max_draw_down(series)) + '%')
    print('Sharpe Ratio:          ' + str(get_sharpe_ratio(series)))
    print('-' * 30)

    fig, ax = plt.subplots(figsize=(20, 5))

    ax.plot((series/series[0]))

    ax.set_title('% Returns')
    ax.set_ylabel('% Return')
    ax.set_xlabel('Date')

    return None