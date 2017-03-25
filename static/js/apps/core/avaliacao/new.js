var tipo = $('#id_swCsvRi');
var tipoDiv = tipo.parent().parent('.form-group');

function hide(list) {
    $.each(list, function(i, e) {
        var id = $('[id^=id_' + e + ']');
        var div = id.parent().parent('.form-group');
        div.fadeOut();
        id.attr("disabled", "disabled");
		id.attr("required", false);
    })
}

function hideAll() {
    list = $('[id^="id_"]');
    $.each(list, function(i, e) {
        if (e.id != 'id_swCsvRi') {
            var id = $('[id^=' + e.id + ']');
            var div = id.parent().parent('.form-group');
            div.fadeOut();
            id.attr("disabled", "disabled");
            id.attr("required", false);
        }
    })
}

function show(list) {
    $.each(list, function(i, e) {
        var id = $('[id^=id_' + e + ']');
        var div = id.parent().parent('.form-group');
        div.fadeIn();
        id.attr("disabled", false);
    })
}

function showAll() {
    list = $('[id^="id_"]');
    $.each(list, function(i, e) {
        var id = $('[id^=' + e.id + ']');
        var div = id.parent().parent('.form-group');
        div.fadeIn();
        id.attr("disabled", false);
    })
}

function visibilityControlTipo() {

    if (tipo.val() == 1) {
        hideAll();
        show(['titulo', 'csv', 'csvDel', 'orientador', 'csvQuo']);
    }else{
        hideAll();
        show(['titulo', 'rawinput','rawinputDel']);
    }

}

$(document).ready(function() {
    tipo.on('change', visibilityControlTipo);

    visibilityControlTipo();
});
