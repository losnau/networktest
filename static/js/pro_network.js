$(document).ready(function () {
            //$('.excuted').click(function () {
            $("body").on('click','.excuted',function() {
         console.log('打印当前节点1'+this);
		 console.log('你点击了执行按钮');
		 method=$(this).attr('id');
		 resultdata=GetReturnValue('status',{"method":method});
		 console.log( resultdata);
		 function GetReturnValue(url, jsonText) {
                   var result = "";
                   $.ajax({
                       type: "POST",
                       url: url,
                       data: jsonText,
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
		 swal({
             title: resultdata["title"],
             text:  resultdata["content"],
             type:  resultdata["type"]
         });
    });
});

// $(function () {
//             $('.excuted').click(function () {
//                 // alert('没有权限下载，请联系管理员！');
//                 console.log($(this).attr('id'));
//                 // var flag = $(this).attr('id');
//                 // alert(flag);
//                 // var filename = $(this).parent().next().find('span').html();
//                 // var dir = $(this).parent().parent().parent().prev().find('a').html();
//                 // $.get('/spider/dataopinfo',{FN:filename,DIR:dir},function (data) {
//                 // data = {key:value}
//                 // data.key
//                 // })
//             })
//         });