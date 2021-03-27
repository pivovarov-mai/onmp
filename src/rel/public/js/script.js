function escapeSpecialChars(jsonString) {
  return jsonString.replace(/\n/g, "\\n")
   .replace(/\r/g, "\\r")
   .replace(/\t/g, "\\t")
   .replace(/\f/g, "\\f")
   .replace(/"/g, '\\"');
}

function currentDate() 
{
	var today = new Date();
	var day = today.getDate();
	day = (day < 10 ? "0" : "") + day;
	var month = today.getMonth();
	month = (month < 10 ? "0" : "") + month;
	var year = today.getFullYear();
	return year+"-"+month+"-"+day;
}

function templateLoad(idcard) {
	$.ajax({
		dataType: "json",
		method: "post",
		url: "/card/"+idcard,
		success: function (data) {
			$.each(data, function(key, val){
				var form_el = "#form"+key;
				var form_obj = $(form_el);
				var form_el_by_val = $(form_el+"[value='"+val+"']");
				var el_type = form_obj.attr("type");
				switch(el_type) {
          case "checkbox":
            if(form_obj.val() == val)
              form_obj.prop("checked", true);
            else
              form_obj.prop("checked", false);
            break;
				  case "radio": 
            form_el_by_val.prop("checked", true);
            break;
			    default: 
            form_obj.val(val);
            break;
        }
			});
			$("#update_order").val("");
			$("#update_comment").val("");
			$("#update_status_draft").prop('checked', true);
			$("#update_status_ready").prop('checked', false);
			$("#update_status_template").prop('checked', false);
			$("#update_status_archive").prop('checked', false);
		},
		error: function() { alert("Error"); }
	});
}

function cardLoad(idcard) {
	$.ajax({
		dataType: "json",
		url: "/card/"+idcard,
		method: "post",
		success: function (data) {
			$.each(data, function(key, val){
				var form_el = "#form"+key;
				var form_obj = $(form_el);
				var form_el_by_val = $(form_el+"[value='"+val+"']");
				var el_type = form_obj.attr("type");
				switch(el_type) {
          case "checkbox":
            if(form_obj.val() == val)
            //if(val != "")
              form_obj.prop("checked", true);
            else
              form_obj.prop("checked", false);
            break;
				  case "radio":
            form_el_by_val.prop("checked", true);
            break;
			    default:
            form_obj.val(val);
            break;
        }
			});
			$("#update_order").val(data["order"]);
			if(data["status"] == 'draft'){
				$("#update_status_draft").prop('checked', true);
			} else {
				$("#update_status_draft").prop('checked', false);
			}
			if(data["status"] == 'ready'){
				$("#update_status_ready").prop('checked', true);
			} else {
				$("#update_status_ready").prop('checked', false);
			}
			if(data["status"] == 'template'){
				$("#update_status_template").prop('checked', true);
			} else {
				$("#update_status_template").prop('checked', false);
			}
			if(data["status"] == 'archive'){
				$("#update_status_archive").prop('checked', true);
			} else {
				$("#update_status_archive").prop('checked', false);
			}
      //alert(data["date"]+" "+data[date]);
			$("#update_comment").val(data["comment"]);
			$("#update_date").val(data["date"]);
		},
		error: function() { alert("Error"); }
	});
}

function cardDelete(idcard)
{
	$.post("/delete/"+idcard);
}

function formEmpty()
{
	for(key=1;key<=132;key++) {
		var form_el = "#form"+key;
		var form_obj = $(form_el);
		//var form_el_by_val = $(form_el+"[value='"+val+"']");
		var el_type = form_obj.attr("type");
		//alert(form_el+" "+el_type);
		switch (el_type) {
      case "radio": radio_obj = $('input:radio[name="'+ key +'"]');
							 radio_obj.prop('checked',false);
							 //radio_obj.data('checked',false);
							 /*if (radio_obj.data("checkboxradio") != undefined)
								obj.prop('checked', false).checkboxradio('refresh');*/ 
							 break;
			case "checkbox": form_obj.prop('checked',false);
							 //form_obj.data('checked',false);
							 /*if (form_obj.data("checkboxradio") != undefined)
								form_obj.prop("checked", false).checkboxradio('refresh');*/
							 break;
      default: form_obj.val("");
							 break;
		}
	}
  $("#update_status_draft").prop('checked', true);
  $("#update_status_ready").prop('checked', false);
  $("#update_status_template").prop('checked', false);
  $("#update_status_archive").prop('checked', false);
}

$(document).on("pageshow", function () {
	$(".zhaloby_content").html("<p>"+$("#form1").val()+"</p>");
	$(".anamnez_content").html("<p>"+$("#form2").val()+"</p>");
	for(key=1;key<=132;key++) {
		var form_el = "#form"+key;
		var form_obj = $(form_el);
		var el_type = form_obj.attr("type");
		switch (el_type) {
         case "radio": radio_obj = $('input:radio[name="'+ key +'"]');
                       try{radio_obj.checkboxradio('refresh');}
                       catch{}
                       break;
			case "checkbox": try{form_obj.checkboxradio('refresh');}
                       catch{}
							         break;
              default: break;
		}
  }
});

$(document).on("pageshow", function () {
	if($.mobile.activePage.attr('id') === "HomePage") {
		$.ajax({
			url: "/draft",
			method: "post",
			success: function(data) {
				$("#draft_listview").html(data);
				$("#draft_listview").listview("refresh");
			}
		});
		$.ajax({
			url: "/ready",
			method: "post",
			success: function(data) {
				$("#ready_listview").html(data);
				$("#ready_listview").listview("refresh");
			}
		});
		$.ajax({
			url: "/template",
			method: "post",
			success: function(data) {
				$("#template_listview").html(data);
				$("#template_listview").listview("refresh");
			}
		});
		$.ajax({
			url: "/archive",
			method: "post",
			success: function(data) {
				$("#archive_listview").html(data);
				$("#archive_listview").listview("refresh");
				$("a.delete").on('click', function() {
					this.closest("li").remove();
					$("#archive_listview").listview("refresh");
				});
			}
		});
	}
});

$(document).ready( function() {
  $('#UpdatePage').on('pagebeforeshow', function () {
    $("#update_status_draft").checkboxradio('refresh');
    $("#update_status_ready").checkboxradio('refresh');
    $("#update_status_template").checkboxradio('refresh');
    $("#update_status_archive").checkboxradio('refresh');
  });
  $('#CreatePage').on('pagebeforeshow', function () {
    $("#order").val("");
    $("#comment").val("");
  });
	$('#update_button').on('click', function(){
		var json = '"order":"'+$('#update_order').val()+'"';
		var json = json+',"date":"'+$('#update_date').val()+'"';
		var json = json+',"status":"'+$("[name='update_status']:checked").val()+'"';
		var json = json+',"comment":"'+$('#update_comment').val()+'"';
		var i;
		for(i=1; i<=132; i++){
			var value = "";
			var form_el = "#form"+i;
			var form_obj = $(form_el);
			var el_type = form_obj.attr("type");
			switch (el_type) {
				case "radio": value = $("[name='"+i+"']:checked").val();
							  if (typeof(value) === "undefined")
                  value = "";
							  break;
				case "checkbox": if(form_obj.prop("checked")) 
								 value = form_obj.val();
								 break;
				default: value = form_obj.val();
                 if (typeof(value) === "undefined")
                  value = "";
						     break;
			}
			/*if(el_type == "radio") {
				 value = $("[name='"+i+"']:checked").val();
				 if (typeof(value) === "undefined")
					 value = "";
			}
			else if (el_type == "checkbox" && )
				value = form_obj.val();;
			else if (el_type == "text" || el_type == "number")
				value = form_obj.val();*/
			json = json+',"'+i+'":"'+escapeSpecialChars(value)+'"';
		}
		json = '{'+json+'}';
    //console.log(json);
		jsonobj = $.parseJSON(json);
		$.ajax({
			url: "/update",
			method: "post",
			data: jsonobj,
			success: function(data) {
				;//alert(data);
			},
			error: function(data){
        alert("error");
				;//alert("ERROR: "+eval(data));
			}
		});
	});
	$('#create_button').on('click', function(){
		$.post("/create", $("#form_create").serialize());
		$("#update_order").val($("#order").val());
		$("#update_comment").val($("#comment").val());
		$("#update_date").val(currentDate());
		//alert("create_button");
	});
	/* toggle the radio buttons
	 */
	$('.radio-toggle').on('click',function(){
		var id = this.id;
		if( $(this).data('checked') ) {
			$(this).prop('checked', false);
			$(this).data('checked', false).checkboxradio('refresh');
			//$(this).prop('checked', false).checkboxradio('refresh');
		} else {
			$(this).data('checked', true).checkboxradio('refresh');
			//$(this).prop('checked', true).checkboxradio('refresh');
		}
		$(':radio[name=' + this.name + ']').not(this).data('checked', false).checkboxradio('refresh');
		//$(':radio[name=' + this.name + ']').not(this).prop('checked', false).checkboxradio('refresh');
	});


	$("input[type=range]").on("keypress", function(e){
	    if ( e.which == 13 ) {
		if ($.mobile.activePage.next("[data-role=page]").length !== 0) {
			var next = $.mobile.activePage.next("[data-role=page]");
			$.mobile.changePage(next, {
			    transition: 'slide'
			});
			return false;
		    } else {
			alert('There\'s no next page');
		    }
		}
	});
	$("input[type=text]").on("keypress", function(e){
	    if ( e.which == 13 ) {
		if ($.mobile.activePage.next("[data-role=page]").length !== 0) {
			var next = $.mobile.activePage.next("[data-role=page]");
			$.mobile.changePage(next, {
			    transition: 'slide'
			});
			return false;
		    } else {
			alert('There\'s no next page');
		    }
		}
	});
	$("input[type=date]").on("keypress", function(e){
	    if ( e.which == 13 ) {
		if ($.mobile.activePage.next("[data-role=page]").length !== 0) {
			var next = $.mobile.activePage.next("[data-role=page]");
			$.mobile.changePage(next, {
			    transition: 'slide'
			});
			return false;
		    } else {
			alert('There\'s no next page');
		    }
		}
	});
	$("select").on('change', function(){
		alert($(this).val());
		var elem = $(this).parent().find('input.form-control');
		var text = elem.val();
		elem.val(text + " " + $(this).children("option:selected").text());
	});
	$('button.add-text').on('click', function(){
		var elem = $(this).parent().find('input.form-control');
		var text = elem.val();
		elem.val(text + " " + $(this).html());
		$(this).html();
	});
	$('.next-input').on('click', function(){
	if ($.mobile.activePage.next("[data-role=page]").length !== 0) {
		var next = $.mobile.activePage.next("[data-role=page]");
		$.mobile.changePage(next, {
		    transition: 'slide'
		});
	    } else {
		alert('There\'s no next page');
	    }
	});
	/*$('button.next-input').on('click', function(){
		$(this).next().val($(this).html());
	});*/
	$('.goforward').on('click', function () {
if ($.mobile.activePage.next("[data-role=page]").length !== 0) {
        var next = $.mobile.activePage.next("[data-role=page]");
        $.mobile.changePage(next, {
            transition: 'slide'
        });
    } else {
        alert('Это последняя страница, следующей нет');
    }
});
	$('.goback').on('click', function () {
if ($.mobile.activePage.prev("[data-role=page]").length !== 0) {
        var prev = $.mobile.activePage.prev("[data-role=page]");
        $.mobile.changePage(prev, {
            transition: 'slide',
            reverse: true
        });
    } else {
        alert('Это первая страница, предыдущей нет');
    }
});
	//$('.form-group').height($(window).height());			
});
