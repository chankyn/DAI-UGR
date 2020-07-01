$(function () {
    // Para quitar la última coma de las tablas si hay varios registros
    $(".comma").each(function(){
        
        var pos = $(this).text().lastIndexOf(',');
        $(this).text($(this).text().substring(0,pos) + " " + $(this).text().substring(pos+1));
    })


    //a -b => cuantos valores se muestran por numero
    var a = 0;
    var b = 4;
    var nRegistros = Math.ceil($("#datos > tbody > tr").length/b);
    
    //Actualizamos la variable "global" con el número de registros que hay.
    $("#nReg").val(nRegistros);

    var button = $('<input type="button"/> ');
    //Botón de primera página y página anterior
    button = $('<input class="moreR" type="button" value = "<<" >');
    button.appendTo($('#registrosArchivados'));
    
    button = $('<input class="moreR" type="button" value = "<" >');
    button.appendTo($('#registrosArchivados'));

    //Creamos los botones intermedios
    for (var i = 1; i <= nRegistros; i++) { 
        button = $('<input class="moreR" type="button" value ='+i+'>');
        button.appendTo($('#registrosArchivados'));
    }
    
    //Botón de última página y página anterior
    button = $('<input class="moreR" type="button" value = ">" >');
    button.appendTo($('#registrosArchivados'));
    
    button = $('<input class="moreR" type="button" value = ">>" >');
    button.appendTo($('#registrosArchivados'));

    //Ocultamos los botones y mostramos solo los 4 primeros (0 a 4)
    $( "#registrosArchivados table > tbody > tr" ).hide();
    $( "#registrosArchivados table > tbody > tr" ).slice( a,b ).show();

    $(".moreR").click(function(){
        //Cambiamos el color cuando pulsamos sobre un botón
        $(".moreR").css('background-color','#DDD');
        $(this).css('background-color','#4eb5f1');

        //Cogemos el valor del botón que se ha pulsado anteriormente y el numero de registros
        var actual = parseInt($("#actual").val(), 10);
        var nReg = parseInt($("#nReg").val(), 10);
        var ini;

        //Calculamos la posición inicial desde donde vamos a mostrar los registros
        $( "#registrosArchivados table > tbody > tr" ).hide();
        switch($(this).val()){
            case "<<": ini = 1;break;
            case "<": ini = actual-1;if (ini < 1 ) ini = 1;break;
            case ">": ini = actual+1;if (ini > nReg ) ini = nReg;break;
            case ">>": ini = nReg;break;
            default:ini = parseInt($(this).val(), 10);
        }        
        
        var fin = ini - 2;
        var aumento = ini + fin;

        aumento = aumento*2;
        $( "#registrosArchivados table > tbody > tr" ).slice( aumento, aumento+b ).show();
        $("#actual").val(ini);
    })

    $('.enlacesAjax').click(function() {
        var id = $(this).attr("name").replace(/[^0-9]/gi, '');
        var tipo = $(this).attr("name").replace(/[^a-z]/gi, '');
        $.get("/reclama_datos", {id: id,tipo: tipo}).done(function(datos){
            // Display the returned data in browser
            Visualiza_datos (datos,tipo);         
        });    
    });
    function Visualiza_datos (datos,tipo) {
        $("#cargarDatosAjax").text("");
        if (tipo == "Album")
            parrafo = '<table class="table"><thead><tr><th>Título del album</th></tr></thead><tbody>';
        else
        parrafo = '<table class="table"><thead><tr><th>Nombre del músico</th></tr></thead><tbody>';
        for (var i = 0; i < datos.resultados.length;i++){
            parrafo +='<tr><td>'+datos.resultados[i]+'</td></tr>';
        }
        parrafo += '</tbody></table>';
        parrafo = $(parrafo);
        parrafo.appendTo($('#cargarDatosAjax'));
        
    };
    
    var cambio = false;
    $("#cambiame").click(function() {
        if (!cambio) {
            $('body').css('font-family', 'tangerine');
            $('div').animate({left: '150px'});
            $('body').css('background-color','#f8f9fa');
            $('label').css('color','#8A2BE2');    
            $('h2').css('color','red');
            $('.btn-danger').addClass("btn-info").removeClass('btn-danger');
            cambio = true;
        }else {
            location.reload();
            cambio = false;
        }
    });
   
    /*
    $.get({
        url: "{% url 'reclama_datos' %}",
        type: 'get',                        
        success: function(datos) {
            Visualiza_datos (datos);  
        },
        failure: function(datos) { 
            alert('esto no vá');
        }
    });
    function Visualiza_datos (datos) {
        alert(datos);
    };
    */
});





