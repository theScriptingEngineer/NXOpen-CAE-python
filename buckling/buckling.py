#nx: threaded

# Buckling provided by theScriptingEngineer

import sys
import math
import NXOpen
import NXOpen.UF
import NXOpen.CAE
from typing import List, cast, Optional, Union

import aiohttp
import asyncio
import json

the_session: NXOpen.Session = NXOpen.Session.GetSession()
base_part = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow

the_uf_session: NXOpen.UF.UFSession = NXOpen.UF.UFSession.GetUFSession()

# buckling parameters
auth = 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjQ1NmI1MmM4MWUzNmZlYWQyNTkyMzFhNjk0N2UwNDBlMDNlYTEyNjIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI1MTI1NjgwMDk5NTgtcXI5YTV2NGNianFjMDJybjF2cmc0NXNhMHZ2YW00YXEuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI1MTI1NjgwMDk5NTgtcXI5YTV2NGNianFjMDJybjF2cmc0NXNhMHZ2YW00YXEuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDYzMzYwODA0MTk5OTY5ODE4ODEiLCJoZCI6InRoZXNjcmlwdGluZ2VuZ2luZWVyLmNvbSIsImVtYWlsIjoidGhlc2NyaXB0aW5nZW5naW5lZXJAdGhlc2NyaXB0aW5nZW5naW5lZXIuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5iZiI6MTcwNDE5Nzc2OCwibmFtZSI6ImZyZWRlcmlrIHZhbmhlZSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NKZ1RYS3VsMUlmWFUwY2JWNlh6VnBQb0wyQ1NLWEJxSTRoOG1lbFZSN2c9czk2LWMiLCJnaXZlbl9uYW1lIjoiZnJlZGVyaWsiLCJmYW1pbHlfbmFtZSI6InZhbmhlZSIsImxvY2FsZSI6ImVuIiwiaWF0IjoxNzA0MTk4MDY4LCJleHAiOjE3MDQyMDE2NjgsImp0aSI6IjFlY2NiNmVkNzkzNGZhMmRhMDcyNDcxOTI1YmE1ZDgxNzQwYmE0MzEifQ.vPIiG7dcBmPl2REw6HPlJ5cHFVKCgW6fVfLnwMhehhG1PwzNzSpqjlcBsOoICO0PjcER2M-z6GtUwiPWmvxSXzIvmk9onB74s0RRAvAdAPe9DUy1Rdl-E1GdQDJMlKctbtAL-8KWbCjHRyQESget1VsoM4zMp_W0hJGEtoAesMSykIFXRANUOzo6bTy0K2Ng87MyQCYR7DN_sTqHNK8tzF8q11g034UwQA-kPLtjw18GZzyyOPo1eXdv_xjGIdXIi9-qAYkFKHwRgQ8nomN5LgNLcf5VM_upes78wO4EeQWzR4bfRt6E2HbsyURzw39Q-X_P8NnQ-8t3qlHMYLRV8A'
url_test_api = 'https://bucklingapi-7rarfy5owa-ew.a.run.app/dnv/stiffenedpaneltest/'
url_test_plate = 'https://bucklingapi-7rarfy5owa-ew.a.run.app/dnv/stiffenedpanel/'
url_test_panel = 'https://bucklingapi-7rarfy5owa-ew.a.run.app/dnv/stiffenedpanel2/'
url = 'http://buckling.theScriptingengineer.com/dnv/stiffenedpanel2/'

test_input_api = {"name":"A stiffened panel","length":10000,"width":3500,"thickness":20}
test_input_plate = {"mat_yield":355000000,"mat_factor":1.15,"span":3.7,"spacing":0.75,"plate_thk":0.018,"stf_web_height":0.4,"stf_web_thk":0.012,"stf_flange_width":0.25,"stf_flange_thk":0.014,"structure_type":"BOTTOM","plate_kpp":1,"stf_kps":1,"stf_km1":12,"stf_km2":24,"stf_km3":12,"sigma_y1":100,"sigma_y2":100,"sigma_x2":102.7,"sigma_x1":102.7,"tau_xy":5,"stf_type":"T","structure_types":"structure_types","zstar_optimization":"true","puls_buckling_method":1,"puls_boundary":"Int","puls_stiffener_end":"C","puls_sp_or_up":"SP","puls_up_boundary":"SSSS","panel_or_shell":"panel","pressure_side":"both sides","girder_lg":5}
test_input_panel = {"Plate":{"mat_yield":355000000,"mat_factor":1.15,"span":3.7,"spacing":0.75,"plate_thk":0.018,"stf_web_height":0.4,"stf_web_thk":0.012,"stf_flange_width":0.25,"stf_flange_thk":0.014,"structure_type":"BOTTOM","plate_kpp":1,"stf_kps":1,"stf_km1":12,"stf_km2":24,"stf_km3":12,"sigma_y1":100,"sigma_y2":100,"sigma_x2":102.7,"sigma_x1":102.7,"tau_xy":5,"stf_type":"T","structure_types":"structure_types","zstar_optimization":"true","puls_buckling_method":1,"puls_boundary":"Int","puls_stiffener_end":"C","puls_sp_or_up":"SP","puls_up_boundary":"SSSS","panel_or_shell":"panel","pressure_side":"both sides","girder_lg":5},"Stiffener":{"mat_yield":355000000,"mat_factor":1.15,"span":3.7,"spacing":0.75,"plate_thk":0.018,"stf_web_height":0.4,"stf_web_thk":0.012,"stf_flange_width":0.25,"stf_flange_thk":0.014,"structure_type":"BOTTOM","plate_kpp":1,"stf_kps":1,"stf_km1":12,"stf_km2":24,"stf_km3":12,"sigma_y1":100,"sigma_y2":100,"sigma_x2":102.7,"sigma_x1":102.7,"tau_xy":5,"stf_type":"T","structure_types":"structure_types","zstar_optimization":"true","puls_buckling_method":1,"puls_boundary":"Int","puls_stiffener_end":"C","puls_sp_or_up":"SP","puls_up_boundary":"SSSS","panel_or_shell":"panel","pressure_side":"both sides","girder_lg":5},"Girder":{"mat_yield":355000000,"mat_factor":1.15,"span":3.7,"spacing":0.75,"plate_thk":0.018,"stf_web_height":0.5,"stf_web_thk":0.012,"stf_flange_width":0.15,"stf_flange_thk":0.02,"structure_type":"BOTTOM","plate_kpp":1,"stf_kps":1,"stf_km1":12,"stf_km2":24,"stf_km3":12,"sigma_y1":80,"sigma_y2":80,"sigma_x2":80,"sigma_x1":80,"tau_xy":5,"stf_type":"T","structure_types":"structure_types","zstar_optimization":"true","puls_buckling_method":2,"puls_boundary":"Int","puls_stiffener_end":"C","puls_sp_or_up":"SP","puls_up_boundary":"SSSS","panel_or_shell":"panel","pressure_side":"both sides","girder_lg":5},"Prescriptive":{"material_yield":355000000,"load_factor_on_stresses":1,"load_factor_on_pressure":1,"buckling_method":"ultimate","stiffener_end_support":"Continuous","girder_end_support":"Continuous","tension_field":"not allowed","plate_effective_against_sigy":"true","km2":24,"km3":12,"pressure_side":"both sides","fabrication_method_stiffener":"welded","fabrication_method_girder":"welded","calculation_domain":"Flat plate, stiffened"},"Pressure":0.412197}

async def make_buckling_request(url, data):
    async with aiohttp.ClientSession() as session:
        headers = {'Content-Type': 'application/json', 'Authorization': auth}
        try:
            async with session.post(url, data=json.dumps(data), headers=headers) as response:
                # Parse the JSON response
                buckling_result = await response.json()
                pretty_json_string = json.dumps(buckling_result, indent=4)        
                
                if response.status == 200:
                    the_lw.Open()
                    the_lw.WriteFullline(pretty_json_string)
                else:
                    # Display an error message if the request was not successful
                    the_lw.Open()
                    the_lw.WriteFullline(f"Error: Unable to fetch buckling result.")
                    the_lw.WriteFullline(f"Status code: {response.status}")
                    the_lw.WriteFullline(pretty_json_string)
        except Exception as e:
            the_lw.Open()
            the_lw.WriteFullline(str(e))

async def main():
    response = await make_buckling_request(url_test_api, test_input_api)
    response = await make_buckling_request(url_test_plate, test_input_plate)
    response = await make_buckling_request(url_test_panel, test_input_panel)

    response = await make_buckling_request(url, url_test_panel)

if __name__ == '__main__':
    asyncio.run(main())
