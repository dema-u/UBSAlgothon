import pandas as pd
import requests
import json

RESOURCE_ENDPOINT = "https://dsa-stg-edp-api.fr-nonprod.aws.thomsonreuters.com/data/historical-pricing/beta1/views/summaries/"
access_token = '26GtCASt7F4X37PrBL1Ml8fcxFwZoCc84afAZThY'


def _get_data_request(url, request_data):
    d_resp = requests.get(url, headers={'X-api-key': access_token}, params=request_data)

    if d_resp.status_code != 200:
        print("Unable to get data. Code %s, Message: %s" % (d_resp.status_code, d_resp.text))
    else:
        print("Data access successful")
        json_resp = json.loads(d_resp.text)
        return json_resp


def get_historical_pricing_data(ric, start_date='2017-01-01', end_date='2018-01-01'):
    """
    Helper function to return a dataframe from historical pricing API
    """

    request_data = {
        "interval": "P1D",
        "start": start_date,
        "end": end_date
    }

    resource_end_point_ric = RESOURCE_ENDPOINT + ric

    json_resp = _get_data_request(resource_end_point_ric, request_data)

    ret_value = None

    if json_resp is not None:
        data = json_resp[0]['data']
        headers = json_resp[0]['headers']
        names = [headers[x]['name'] for x in range(len(headers))]
        ret_value = pd.DataFrame(data, columns=names)
    else:
        print('no data for RIC={0}'.format(ric))

    ret_value.set_index(pd.to_datetime(ret_value['DATE']), inplace=True)
    ret_value = ret_value[::-1]

    return ret_value
