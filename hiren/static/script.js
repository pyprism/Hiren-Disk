/**
 * Created by prism on 8/27/14.
 */
$(document).ready(function() {
    if(simpleStorage.get('disk')){
        $('#disk').val(simpleStorage.get('disk'))
    }
    if(simpleStorage.get('box')){
        $('#box').val(simpleStorage.get('box'))
    }

    $( "#add" ).click(function( event ) {
       event.preventDefault();
       simpleStorage.set("disk", $('#disk').val, {TTL: 100000});
       simpleStorage.set("box", $('#box').val, {TTL: 100000});
    });
});