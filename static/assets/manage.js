

$(document).ready(function(){
   
    window.addEventListener("hashchange",switchTabs)
    switchTabs()
    function getQueryParameter(name) {
        let urlParams = new URLSearchParams(window.location.search);
        return urlParams.get(name);
    }

    
    function switchTabs(e){
        let eventId = getQueryParameter('event_id');
        //console.log($(e.target));
        let hash = location.hash;
        hash = hash.replace("#/","")
        //hash = hash.replace("/","")
        console.log(hash)
        if(hash.length == 0){return}
        const multitabs = document.getElementById('multitabs')
        const cards = multitabs.getElementsByClassName('card-body');
        const links = document.getElementsByClassName('nav-link')
        for(const link of links){
            if(link.classList.contains('router-link-active')){
                link.classList.remove('active')
                link.classList.remove('router-link-active')
            }
            //console.log(link.href)
            if(link.href.includes('#'+hash)){
                link.classList.add('active')
                link.classList.add('router-link-active')
            }
        }
        for(const card of cards){
            card.style.display = 'none'
            if(card.id == '#'+hash){
                card.style.display = ''
            }
        }
        if (eventId) {
            $('input[name="event_id"]').val(eventId);
        }
    }
    let eventId = getQueryParameter('event_id');
    fetch('/template/details.html?event_id='+eventId)
        .then(response => response.text())
        .then(data => {
            // Insert the HTML content into the placeholder element
            $('#load-details').html(data);
        })
        .catch(error => console.error('Error loading HTML snippet:', error));
    fetch('/template/timing.html?event_id='+eventId)
        .then(response => response.text())
        .then(data => {
            // Insert the HTML content into the placeholder element
            $('#load-timing').html(data);
        })
        .catch(error => console.error('Error loading HTML snippet:', error));
    fetch('/template/tickets.html?event_id='+eventId)
        .then(response => response.text())
        .then(data => {
            // Insert the HTML content into the placeholder element
            $('#load-tickets').html(data);
        })
        .catch(error => console.error('Error loading HTML snippet:', error));
    fetch('/template/location.html?event_id='+eventId)
        .then(response => response.text())
        .then(data => {
            // Insert the HTML content into the placeholder element
            $('#load-location').html(data);
        })
        .catch(error => console.error('Error loading HTML snippet:', error));
    fetch('/template/media.html?event_id='+eventId)
        .then(response => response.text())
        .then(data => {
            // Insert the HTML content into the placeholder element
           $('#load-media').html(data);
        })
        .catch(error => console.error('Error loading HTML snippet:', error));
    fetch('/template/seo.html?event_id='+eventId)
        .then(response => response.text())
        .then(data => {
            // Insert the HTML content into the placeholder element
           $('#load-seo').html(data);
        })
        .catch(error => console.error('Error loading HTML snippet:', error));
    fetch('/template/publish.html?event_id='+eventId)
        .then(response => response.text())
        .then(data => {
            // Insert the HTML content into the placeholder element
            $('#load-publish').html(data);
        })
        .catch(error => console.error('Error loading HTML snippet:', error));

        $('#event_title').on('keyup',function(){
        
            let url = $(this).val()
            url = url.replace(/\s+/g,"-")
            url = url.toLowerCase()
            console.log(url)
            $('.event_slug').val(url)
    
        })
        $('.select_tags').on('change',function(){
            val = $(this).val()
            $("tags").val($("#tags").val()+";"+val);
        })
})