import re
import CUBRIDdb
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# _id [0] rdnmadr [11]

#DB연결 
conn = CUBRIDdb.connect('CUBRID:13.124.197.219:30000:IROSDB:::','soa','soa')

#cursor는 fetch동작 관리, cur은 객체
cur = conn.cursor()

tableList=[ "tn_pubr_public_prhsmk_zn_api"]

tableList=["tn_pubr_public_acdnt_area_api",
"tn_pubr_public_aed_api",
'tn_pubr_public_animal_cnter_api',
 "tn_pubr_public_appn_mnrlsp_info_api",
 'tn_pubr_public_area_spcliz_stret_api',
 "tn_pubr_public_auto_maintenance_company_api",
 'tn_pubr_public_bcycl_dpstry_api',
 'tn_pubr_public_bcycl_lend_api']
# 'tn_pubr_public_campg_api',
# 'tn_pubr_public_car_inspofc_api',
# 'tn_pubr_public_car_rental_api',
# 'tn_pubr_public_carwsh_api',
# 'tn_pubr_public_cctv_api',
# 'tn_pubr_public_child_prtc_zn_api',
# 'tn_pubr_public_clns_shunt_fclty_api',
# 'tn_pubr_public_cltur_fstvl_api',
# 'tn_pubr_public_crosswalk_api',
# 'tn_pubr_public_cty_park_info_api',
# 'tn_pubr_public_ctyrlroad_statn_api',
# 'tn_pubr_public_drowsy_shelter_api',
# 'tn_pubr_public_elcty_car_chrstn_api'
# 'tn_pubr_public_elesch_mskul_lc_api',
# 'tn_pubr_public_food_truck_permit_area_api',
# 'tn_pubr_public_frcn_rent_info_api',
# 'tn_pubr_public_free_mlsv_api',
# 'tn_pubr_public_free_wrlsfd_api',
# 'tn_pubr_public_frfire_risk_area_api',
# 'tn_pubr_public_frhl_exprn_vilage_api',
# 'tn_pubr_public_fshlc_api',
# 'tn_pubr_public_grund_snkg_api',
# 'tn_pubr_public_heat_wve_shltr_api',
# 'tn_pubr_public_hp_cnter_api',
# 'tn_pubr_public_imbclty_cnter_api',
# 'tn_pubr_public_lbrry_api',
# 'tn_pubr_public_mnlss_cvpl_issu_info_api',
# 'tn_pubr_public_museum_artgr_info_api',
# 'tn_pubr_public_nrstr_api',
# 'tn_pubr_public_nvpc_cltur_relics_api',
# 'tn_pubr_public_overpass_api',
# 'tn_pubr_public_ovrspd_prvn_manage_api',
# 'tn_pubr_public_pblfclt_opn_info_api',
# 'tn_pubr_public_pblprfr_event_info_api',
# 'tn_pubr_public_pnsn_bssh_api',
# 'tn_pubr_public_prhsmk_zn_api',
# 'tn_pubr_public_rcrfrst_api',
# 'tn_pubr_public_residnt_prior_parkng_api',
# 'tn_pubr_public_rest_area_api',
# 'tn_pubr_public_road_drcbrd_examin_api',
# 'tn_pubr_public_road_safety_mark_api',
# 'tn_pubr_public_ruse_cnter_api',
# 'tn_pubr_public_safety_emergency_bell_position_api',
# 'tn_pubr_public_scrty_lmp_api',
# 'tn_pubr_public_shelter_api',
# 'tn_pubr_public_small_pblfclt_risk_appn_api',
# 'tn_pubr_public_smart_streetlight_api',
# 'tn_pubr_public_stret_tursm_info_api',
# 'tn_pubr_public_tfcwker_mvmn_cnter_api',
# 'tn_pubr_public_toilet_api',
# 'tn_pubr_public_towng_vhcle_dpstry_api',
# 'tn_pubr_public_traffic_light_api',
# 'tn_pubr_public_trdit_mrkt_api',
# 'tn_pubr_public_trrsrt_api',
# 'tn_pubr_public_unmanned_traffic_camera_api',
# ]



for table in tableList:
    try:
        query = "select * from {0}".format(table)
        #query = "select _id, rdnmadr from tn_pubr_public_prhsmk_zn_api where rdnmadr  like '%''%' limit 100"
        cur.execute(query)
        
        #한개의 row만 가져오기
        row = cur.fetchone()

        while row:
            for str in row:

                #string 타입이면
                if(type(str)==type("")):
                    #'' 를 찾으면 ''제거
                    if(str.find("\'\'") != -1):
                        print(str)
                        print(re.sub("\'","",str))

                    #""를 찾으면 ""제거
                    elif str.find("\"\"") != -1:
                        print(str)
                        print(re.sub("\'","",str))

            row=cur.fetchone()


    except Exception as e:
        print(e)

print("끝")


#query문 실행
#cur.execute("select * from tn_pubr_public_prhsmk_zn_api where rdnmadr like '%''%' limit 100")

#한개의 row만 가져오기
#row = cur.fetchone()

#수정된 문자열을 저장할 객체 생성
#modifyList=[]

#while row:
#    modifyList.append(row)
#    row = cur.fetchone()

#for modify in modifyList:
    # ' 제거
#    modify[11] = re.sub("\'","","".join(modify[11]))

#    query="UPDATE tn_pubr_public_prhsmk_zn_api SET rdnmadr ='{0}' WHERE _id = {1}".format(modify[11],modify[0])

#print(query)



# #한 줄 씩 출력
# for list in modifyList:
#     print(list)

#for query in modifyList:



#conn.commit()