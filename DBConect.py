import re
import CUBRIDdb
import logging
from datetime import datetime
from flask import Flask

#08.12 리눅스 서버에서 코드 배포하기위해 준비(환경설정)
# 로그 생성
logger = logging.getLogger()

# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)

# log 출력 형식
formatter = logging.Formatter('%(asctime)s - [%(levelname)s  ] - %(message)s')

# log 출력
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

today=datetime.today()


# log를 파일에 출력
file_handler = logging.FileHandler('{0}.log'.format(str(datetime.today())[:10]),encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

app = Flask(__name__)

def making_dictionary(table_dictionary, row , columList) :
    for colum,index in zip(columList,range(len(row))) :
        table_dictionary[colum]=row[index]

def find_key(dict, val):
  return next(key for key, value in dict.items() if value == val)

def string_check(table_dictionary):

    dic_values=list(table_dictionary.values())
    modify_key_list=[]

    for string in dic_values:
        if(type(string)==type("")):
            #'' 를 찾으면 ''제거
            string = str(string)
            if(string.find("\'\'") != -1):
                modify_str = re.sub("\'","",string)
                key=find_key(table_dictionary,string)
                table_dictionary[key]=modify_str
                modify_key_list.append(key)
                logger.info("바뀔문장 : {0}".format(string))

            #""을 찾으면 "제거
            if string.find("\"\"") != -1:
                modify_str = re.sub("\"","",string)
                key=find_key(table_dictionary,string)
                table_dictionary[key]=modify_str
                modify_key_list.append(key)
                logger.info("바뀔문장 : {0}".format(string))

    return modify_key_list



@app.route('/')
def home():
    return 'Hello, World!!'


@app.route('/modify')
def modify_row():
    
    #DB연결 
    conn = CUBRIDdb.connect('CUBRID:13.124.197.219:30000:IROSDB:::','soa','soa')

    #cursor는 fetch동작 관리, cur은 객체
    cur = conn.cursor()

    table_list=[
    "tn_pubr_public_acdnt_area_api",
    "tn_pubr_public_aed_api",
    'tn_pubr_public_animal_cnter_api',
    "tn_pubr_public_appn_mnrlsp_info_api",
    'tn_pubr_public_area_spcliz_stret_api',
    "tn_pubr_public_auto_maintenance_company_api",
    'tn_pubr_public_bcycl_dpstry_api',
    'tn_pubr_public_bcycl_lend_api',
    'tn_pubr_public_campg_api',
    'tn_pubr_public_car_inspofc_api',
    'tn_pubr_public_car_rental_api',
    'tn_pubr_public_carwsh_api',
    'tn_pubr_public_cctv_api',
    'tn_pubr_public_child_prtc_zn_api',
    'tn_pubr_public_clns_shunt_fclty_api',
    'tn_pubr_public_cltur_fstvl_api',
    'tn_pubr_public_crosswalk_api',
    'tn_pubr_public_cty_park_info_api',
    'tn_pubr_public_ctyrlroad_statn_api',
    'tn_pubr_public_drowsy_shelter_api',
    'tn_pubr_public_elcty_car_chrstn_api'
    'tn_pubr_public_elesch_mskul_lc_api',
    'tn_pubr_public_food_truck_permit_area_api',
    'tn_pubr_public_frcn_rent_info_api',
    'tn_pubr_public_free_mlsv_api',
    'tn_pubr_public_free_wrlsfd_api',
    'tn_pubr_public_frfire_risk_area_api',
    'tn_pubr_public_frhl_exprn_vilage_api',
    'tn_pubr_public_fshlc_api',
    'tn_pubr_public_grund_snkg_api',
    'tn_pubr_public_heat_wve_shltr_api',
    'tn_pubr_public_hp_cnter_api',
    'tn_pubr_public_imbclty_cnter_api',
    'tn_pubr_public_lbrry_api',
    'tn_pubr_public_mnlss_cvpl_issu_info_api',
    'tn_pubr_public_museum_artgr_info_api',
    'tn_pubr_public_nrstr_api',
    'tn_pubr_public_nvpc_cltur_relics_api',
    'tn_pubr_public_overpass_api',
    'tn_pubr_public_ovrspd_prvn_manage_api',
    'tn_pubr_public_pblfclt_opn_info_api',
    'tn_pubr_public_pblprfr_event_info_api',
    'tn_pubr_public_pnsn_bssh_api',
    'tn_pubr_public_prhsmk_zn_api',
    'tn_pubr_public_rcrfrst_api',
    'tn_pubr_public_residnt_prior_parkng_api',
    'tn_pubr_public_rest_area_api',
    'tn_pubr_public_road_drcbrd_examin_api',
    'tn_pubr_public_road_safety_mark_api',
    'tn_pubr_public_ruse_cnter_api',
    'tn_pubr_public_safety_emergency_bell_position_api',
    'tn_pubr_public_scrty_lmp_api',
    'tn_pubr_public_shelter_api',
    'tn_pubr_public_small_pblfclt_risk_appn_api',
    'tn_pubr_public_smart_streetlight_api',
    'tn_pubr_public_stret_tursm_info_api',
    'tn_pubr_public_tfcwker_mvmn_cnter_api',
    'tn_pubr_public_toilet_api',
    'tn_pubr_public_towng_vhcle_dpstry_api',
    'tn_pubr_public_traffic_light_api',
    'tn_pubr_public_trdit_mrkt_api',
    'tn_pubr_public_trrsrt_api',
    'tn_pubr_public_unmanned_traffic_camera_api',
    ]

    for table in table_list:
        try:
            query = "desc {0}".format(table)
            cur.execute(query)
            column_row = cur.fetchall()
            colum_list=[]
            table_dictionary={}
            modify_key_list=[]


            for colum in column_row:
                colum_list.append(colum[0])

            query = "select * from {0}".format(table)
            cur.execute(query)

            rows = cur.fetchall()

            for row in rows:
                making_dictionary(table_dictionary,row,colum_list)
                modify_key_list = string_check(table_dictionary)
                for colum in modify_key_list:
                    updateQuery = "update {0} set {1} ='{2}' where _id = {3}".format(table,colum,table_dictionary[colum],row[0])
                    logger.info("_ID : {0}".format(row[0]))
                    logger.info("TABLE : {0}".format(table))
                    logger.info("QUERY : {0}".format(updateQuery))
                    logger.info("=========================================================================")    
                    
            
            table_dictionary.clear()

        except Exception as e:
            logger.warning(e)
    
    return "Finsh"



#debug=True로 명시하면 해당 파일의 코드를 수정할 때 마다 Flask가 변경된 것을 인식하고 다시
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '49152' ,debug=True)