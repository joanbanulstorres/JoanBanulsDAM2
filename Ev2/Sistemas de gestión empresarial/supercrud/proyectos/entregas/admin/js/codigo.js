$(document).ready(function(){
	
	$("td").dblclick(function(){
		
		// Utilizando la librería SELECT2
		$('select').select2();					
		// Cuando se inserte en el 'body' un elemento de tipo select, le aplica el select2
		$('body').on('DOMNodeInserted', 'select', function(){
			$(this).select2().on('select2:select', function(e){
				var data = e.params.data;	                         // Se coge la data de la asignatura seleccionada
				var valoraenviar = data.id;
				var texto = data.text;
				var tabla = $(this).parent().attr("tabla");
				var columna = $(this).parent().attr("columna");
				var identificador = $(this).parent().attr('identificador');
				console.log("Se va a insertar el valor " + valoraenviar + " en el registro con el id " + identificador + ", de la columna " + columna + ", de la tabla " + tabla);
				$("#ajax").load("inc/ajaxmodifica.php?valor="+valoraenviar+"&tabla="+tabla+"&columna="+columna+"&identificador="+identificador);
				$(this).parent().html("<td><b>"+valoraenviar+"</b> - "+texto+"</td>");
			});
		});
		
		if($(this).attr('externo') == "no"){
			var selector;
			$(this).attr('contenteditable', 'true').blur(function(){
				selector = $(this);
				selector.attr('contenteditable', 'false');
				var valoraenviar = selector.text();
				var tabla = selector.attr("tabla");
				var columna = selector.attr("columna");
				var identificador = selector.attr('identificador');
				console.log("Se va a insertar el valor " + valoraenviar + " en el registro con el id " + identificador + ", de la columna " + columna + ", de la tabla " + tabla);
				$("#ajax").load("inc/ajaxmodifica.php?valor="+valoraenviar+"&tabla="+tabla+"&columna="+columna+"&identificador="+identificador);
			});
		}
		
		if($(this).attr('externo') == "si"){
			selector = $(this);
			var tabla = selector.attr("tablaexterna");
			var columna = selector.attr("columnaexterna");
			var claveexterna = selector.attr("claveexterna");
			$(this).load("inc/ajaxvalores.php?tabla="+tabla+"&columna="+columna+"&claveexterna="+claveexterna);
			$('select').select2();
		}
	});
})