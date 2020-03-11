// This file will add target='_blank' attribute to 
// sharepoint calendar link in the menu

// external links in top bar:
$('nav#nav a[href*="http"]').each( function() {
    $(this).attr('target','_blank');
});

// external links in drop menus bar:
$('ul.dropotron a[href*="http"]').each( function() {
    $(this).attr('target','_blank');
});

$(document).ready(function() {
    // link in side bar (when screen is narrow):
    // only works if you wait until everything has been loaded 
    // (unlike above for the top menu that works right away)
    $( "<i class='fa fa-calendar menu-fa'></i>" ).insertAfter('div#navPanel a[href*="default.aspx"]> span');
    $( "<i class='fa fa-search menu-fa'></i>" ).insertAfter('div#navPanel a[href*="explore/keyword"]> span');
    $('div#navPanel a[href*="http"]').each( function() {
        $(this).attr('target','_blank');
    });
});

