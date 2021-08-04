import re
import CUBRIDdb

def makingDictionary(tableDictionary, row , columList) :
    for colum,index in zip(columList,range(len(row))) :
        tableDictionary[colum]=row[index]

def findKey(dict, val):
  return next(key for key, value in dict.items() if value == val)

def stringcheck(tableDictionary):

    dicValues=list(tableDictionary.values())
    modifyKeyList=[]

    for string in dicValues:
        if(type(string)==type("")):
            #'' 를 찾으면 ''제거
            string = str(string)
            if(string.find("\'\'") != -1):
                modifyStr = re.sub("\'","",string)
                key=findKey(tableDictionary,string)
                tableDictionary[key]=modifyStr
                modifyKeyList.append(key)
                print(string)

            #""을 찾으면 "제거
            if string.find("\"\"") != -1:
                modifyStr = re.sub("\"","",string)
                key=findKey(tableDictionary,string)
                tableDictionary[key]=modifyStr
                modifyKeyList.append(key)
                print(string)

    return modifyKeyList



#DB연결 
conn = CUBRIDdb.connect('CUBRID:13.124.197.219:30000:IROSDB:::','soa','soa')

#cursor는 fetch동작 관리, cur은 객체
cur = conn.cursor()

tableList=[
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


for table in tableList:
    try:
        query = "desc {0}".format(table)
        cur.execute(query)
        columnRow = cur.fetchall()
        columList=[]
        tableDictionary={}
        modifyKeyList=[]

        for colum in columnRow:
            columList.append(colum[0])

        query = "select * from {0}".format(table)
        #query = "select _id, rdnmadr from tn_pubr_public_prhsmk_zn_api where rdnmadr  like '%''%' limit 100"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            makingDictionary(tableDictionary,row,columList)
            modifyKeyList = stringcheck(tableDictionary)
            for colum in modifyKeyList:
                updateQuery = "update {0} set {1} ='{2}'".format(table,colum,tableDictionary[colum])
                print(updateQuery)    
        
        tableDictionary.clear()


    except Exception as e:
        print(e)

print("끝")

# query = "desc tn_pubr_public_prhsmk_zn_api"
# cur.execute(query)
# columnRow = cur.fetchall()
# columList=[]
# tableDictionary={}
 
# for colum in columnRow:
#     columList.append(colum[0])

# query = "select _id, rdnmadr from tn_pubr_public_prhsmk_zn_api where rdnmadr  like '%''%' limit 100"
# cur.execute(query)

# row = cur.fetchone()
        
# tableDictionary=makingDictionary(tableDictionary,row,columList)
# print(tableDictionary)
# stringcheck(tableDictionary)
# print(tableDictionary)

#conn.commit()