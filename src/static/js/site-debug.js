$(ready);
function ready(){
    $("#wmd-preview").hide();
    $('#lnkPreview').click(function(){
	toggle_preview();
    });
}

function toggle_preview(){
    $("#wmd-preview").toggle();
}
