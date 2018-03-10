var EditableTable = function () {
    return {
        //初始化模块
        init: function () {
            var oTable = $('#usermanager_table').DataTable({
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
                "searching": false,
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
                    {"width": "25%" , 'aTargets': [0]},
                    {"width": "25%" , 'aTargets': [1]},
                    {"width": "10%" , 'aTargets': [2]},
                    {"width": "10%" ,'aTargets': [3]},
                    {"width": "10%" , 'aTargets': [4]},
                    {"width": "10%" ,'aTargets': [5]},
                    {"width": "10%" ,'aTargets': [6]},
                    {"bVisible": false, "bSearchable": false, 'aTargets': [7]}

                ]
            });

            jQuery('#editable-sample_wrapper .dataTables_filter input').addClass("form-control medium"); // modify table search input
            jQuery('#editable-sample_wrapper .dataTables_length select').addClass("form-control xsmall"); // modify table per page dropdown
            function saveRow(oTable, nRow) {
                var jqInputs = $('input', nRow);
                //获取老的数据，从里面读取ID的值
                //console.log('打印老的数据：',jqInputs )
                var oldData = oTable.row(nRow).data();
                edata=[jqInputs[0].value,jqInputs[1].value,jqInputs[2].value,jqInputs[3].value,'<a class="edit" href="javascript:;">编辑</a>',
                    '<a class="delete" href="javascript:;">删除</a>','<td><a class="resetpasswd" href="resetpasswd">重置密码</a></td>',oldData [7]]
                oTable.row(nRow).data(edata);
				//  jqInputs当前编辑行的数据，           这个数值表示在表格中的位置
                oTable.draw();
            }
            //点击编辑按钮
            function editRow(oTable, nRow) {
                var aData = oTable.row(nRow).data();
                var jqTds = $('>td', nRow);
                // console.log(aData)
                // console.log(aData[0])
                // console.log(aData[12])
                // console.log(aData[13])
                jqTds[0].innerHTML = '<input type="text" data-field=="nickname" class="form-control small"  value="' + aData[0] + '">';
                jqTds[1].innerHTML = '<input type="text" data-field=="username" class="form-control small"  value="' + aData[1] + '">';
                jqTds[2].innerHTML = '<input type="text" data-field="is_superuser" class="form-control small" value="' + aData[2] + '">';
                jqTds[3].innerHTML = '<input type="text" data-field="is_disabled" class="form-control small" value="' + aData[3] + '">';
                jqTds[4].innerHTML = '<a class="edit" href=javascript:"">保存</a>';
                jqTds[5].innerHTML = '<a class="cancel" href="javascript:">取消</a>';

            }
                        //编辑取消时重新加载当前行
            function restoreRow(oTable, nRow) {
                var aData = oTable.row(nRow).data();
                oTable.row(nRow).data(aData);
                oTable.draw();
            }
            var nEditing = null;
             $('#usermanager_table a.cancel').live('click', function (e) {
                console.log('点击了取消按钮');
                e.preventDefault();
                //如果表格是新行，点击取消编辑就删掉这一行
                if ($(this).attr("data-mode") == "new") {
                    var nRow = $(this).parents('tr')[0];
                    oTable.row(nRow).remove();
                    oTable.draw();
                    nEditing=null;
                } else {
                    console.log('有数据');
                 //如果表格有数据，恢复表格数据
                    restoreRow(oTable, nEditing);
                    nEditing = null;

                }
            });
            $('#usermanager_table a.edit').live('click', function (e) {
                e.preventDefault();
                /* Get the row as a parent of the link that was clicked on */
                var nRow = $(this).parents('tr')[0];
                if (nEditing !== null && nEditing != nRow) {
                    /* 目前正在编辑 - 但不是这一行 - 在继续编辑模式之前恢复旧的 */
                    restoreRow(oTable, nEditing);
                    editRow(oTable, nRow);
                    nEditing = nRow;
                } else if (nEditing == nRow && this.innerHTML == "保存") {
                    /* Editing this row and want to save it */
                    saveRow(oTable, nEditing);
                    var eData = oTable.row(nRow).data();     //获取数据
                    console.log('打印编辑行的数据：',eData)
                    nEditing = null;
                     $.ajax({
                        url: "save",
                         data: {"nickname": eData[0],"username": eData[1],"is_superuser": eData[2],"is_disabled": eData[3],"userid": eData[7]},
                         type: "post"
                    });
                    //alert("Updated! Do not forget to do some ajax to sync with backend :)");
                } else {
                    /* No edit in progress - let's start one */
                    editRow(oTable, nRow);
                    nEditing = nRow;
                }
            });
                        //点击删除按钮
            $('#usermanager_table a.delete').live('click', function (e) {
                e.preventDefault();

                if (confirm("Are you sure to delete this row ?") == false) {
                    return;
                }
                console.log('点击了删除按钮');
                var nRow = $(this).parents('tr')[0];
                var eData =  oTable.row(nRow).data();     //获取数据
                oTable.row(nRow).remove();
                oTable.draw()
                $.ajax({
                    url: "delete",
                    data: {"userid": eData[7]},
                    type: "post"
                });
            });
            // $('#usermanager_table a.resetpasswd').live('click', function (e) {
            //     console.log('点击了重置密码按钮');
            //     var nRow = $(this).parents('tr')[0];
            //     var eData =  oTable.row(nRow).data();     //获取数据
            //     $.ajax({
            //         url: "resetuserpd",
            //         data: {"userid": eData[7]},
            //         type: "get"
            //     });
            // });
        }
    };
}();