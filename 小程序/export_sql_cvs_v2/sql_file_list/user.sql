SELECT bu.id AS id,
 bu.business_key AS businessKey,
 bu.pass_word AS passWord,
 bu.create_time AS createTime,
 bu.device_number AS deviceNumber,
 bu.email AS email,
 bu.id_card AS idCard,
 bu.ji_num AS jiNum,
 bu.telphone AS telphone,
 bu.category AS category,
 bu.update_time AS updateTime,
 bu.user_code AS userCode,
 bu.birthday AS birthday,
 bu.name AS name,
 bu.phone AS phone,
 bu.sex AS sex,
 bu.nickname AS nickname,
 bu.status_type AS statusType,
 bu.is_delete AS isDelete
FROM base_user bu
WHERE bu.category = 'ordinaryUser'