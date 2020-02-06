// This file will add a calendar icon and target='_blank' attribute to 
// sharepoint calendar link in the menu

// link in top bar:
$('nav#nav a[href*="msed/MSED-MMF/default.aspx"]').replaceWith(
    '<a target="_blank" href="https://mmlshare.nist.gov/Div/msed/MSED-MMF/default.aspx"><i class="fa fa-calendar"></i><span style="margin-right:5px;"></span>Sharepoint Calendar</a>'
)

$(document).ready(function() {
    // link in side bar (when screen is narrow):
    // only works if you wait until everything has been loaded 
    // (unlike above for the top menu that works right away)
    $( "<i class='fa fa-calendar'></i><span style='margin-right:5px;'></span>" ).insertAfter('div#navPanel a[href*="msed/MSED-MMF/default.aspx"]> span');
});

