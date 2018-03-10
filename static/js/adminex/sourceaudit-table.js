var EditableTable = function () {
    return {
        //初始化模块
        init: function () {
            var oTable = $('#sourceaudit_table').DataTable({
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
                "searching": true,
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
                    {"width": "20%" , 'aTargets': [0]},
                    {"width": "20%" , 'aTargets': [1]},
                    {"width": "10%" , 'aTargets': [2]},
                    {"width": "10%" ,'aTargets': [3]},
                    {"width": "10%" , 'aTargets': [4]},
                    {"width": "20%" , 'aTargets': [5]},
                    {"width": "10%" , 'aTargets': [5]}
                ]

            });
        }
    };
}();