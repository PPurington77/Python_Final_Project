function initMap() {
    //map options
    var options = {
        zoom : 14, 
        center : {lat:29.783855616912607, lng:-82.03078825534682}
    }
    //new map
    var map = new google.maps.Map(document.getElementById('map'), options);
    //add marker
    var marker = new google.maps.Marker({
        position: {lat:29.783855616912607, lng:-82.03078825534682}, map:map, icon:'/static/images/favicon-32x32.png'
    })
}
