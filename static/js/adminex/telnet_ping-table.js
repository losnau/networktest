var EditableTable = function () {
    return {
        //初始化模块
        init: function () {
            var oTable = $('#editable-sample').DataTable({
                "aLengthMenu": [
                    [10, 20, 30, -1],
                    [10, 20, 30, "All"] // change per page values here
                ],
                 //因为默认第一列升序排列，所以根据代码，新加的行第一列是累加的，那么越来越大，升序的话当然往后面排啊
                "order": [[0, "des"]],
                "sDom": "<'row'<'col-lg-6'l><'col-lg-6'f>r>t<'row'<'col-lg-6'i><'col-lg-6'p>>",
                "sPaginationType": "bootstrap",
                "bSort":true,
                "stateSave" : false,
                "language": {//国际化
                     "lengthMenu":"每页显示_MENU_条记录",
                        "info":"当前显示第_START_至_END_条记录(总记录数_TOTAL_条)",
                        "infoFiltered":"",
                        "infoEmpty":"总记录数 0",
                        "search":"搜索",
                        "processing":"载入中...",
                        "emptyTable":"无数据",
                        "paginate":{
                            "first":"第一页",
                            "previous":"上一页",
                            "next":"下一页",
                            "last":"最后一页"
                        }
                                },
                //列渲染，可以添加一些操作等
                "aoColumnDefs": [
                //    {"bVisible": false, "bSearchable": false, 'aTargets': [2]},
                    {"visible": false,  'targets':0 },
                  //  {"width": "10",  'targets':0 },
                    {"width": "25%" , 'targets': 1},
                 //   {"width": "20%" , 'aTargets': 2},
                    {"visible": false , 'aTargets': 2},
                    {"width": "10%" , 'aTargets': 3},
                    {"width": "20%" ,'aTargets': 4},
                    {"width": "20%" , 'aTargets': 5},
                    {"width": "15%" , 'aTargets': 6}
                ],
                searching: true
            });
            $(document).ready(function () {
            //$('.excuted').click(function () {
            $("body").on('click','.excuted',function() {
		 function GetReturnValue(url, jsonText) {
                   var result = "";
                   $.ajax({
                       type: "POST",
                       url: url,
                       data: jsonText,
                       // contentType: "application/json;charset=utf-8",
                       // dataType: "json",
                       async: false,//同步
                       success: function (data) {
                           result = data;
                           console.log("result:"+result)
                       }, failure: function () {
                           result = "";
                       }
                   });
                   return result;
                }
		console.log('你点击了执行按钮');
                var nRow = $(this).parents('tr')[0];
                var aData = oTable.row(nRow).data();
                // console.log('选择源IP：'+$('#choose-sourceip option:selected').val());
                // console.log('搜索测试方式：'+$('#choose-temethod option:selected').val());
                var choosesourceip='#choose-sourceip'+aData[0]+' option:selected'
                var choosetemethod='#choose-temethod'+aData[0]+' option:selected'
                var sourceip=$(choosesourceip).val()
                var temethod=$(choosetemethod).val()
                console.log(choosesourceip)
                console.log(sourceip)
                console.log(temethod)
                if (temethod == '' || temethod=='' ){
                    alert('请选择源地址或者测试方法');
                }
                // console.log(aData[0])
                // console.log(aData[1])
                // console.log(aData[3])
                // console.log(aData[4])
                // console.log(aData[5])
                resultdata=GetReturnValue('checkpt',{"sourceip":sourceip,"temethod":temethod,"sourcenam":aData[1],"host":aData[2],"port":aData[3]})
                console.log( resultdata)
                swal({
                    title: resultdata["title"],
                    text:  resultdata["content"],
                    type:  resultdata["type"]
                });
            });
        });
        }
    };
}();
