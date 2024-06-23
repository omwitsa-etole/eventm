

$(document).ready(function(){
    window.addEventListener("hashchange",switchTabs)
    switchTabs()
    $('.event-name').on('keyup',function(e){
        
        let url = $(this).val()
        url = url.replace(" ","-")
        url = url.toLowerCase()
        console.log(url)
        $('.event-url').val(url)

    })
    function switchTabs(e){
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

    }
    fetch('/template/timing.html')
        .then(response => response.text())
        .then(data => {
            // Insert the HTML content into the placeholder element
            $('#load-timing').html(data);
        })
        .catch(error => console.error('Error loading HTML snippet:', error));
    fetch('/template/tickets.html')
        .then(response => response.text())
        .then(data => {
            // Insert the HTML content into the placeholder element
            $('#load-tickets').html(data);
        })
        .catch(error => console.error('Error loading HTML snippet:', error));
    fetch('/template/location.html')
        .then(response => response.text())
        .then(data => {
            // Insert the HTML content into the placeholder element
            $('#load-location').html(data);
        })
        .catch(error => console.error('Error loading HTML snippet:', error));
    fetch('/template/media.html')
        .then(response => response.text())
        .then(data => {
            // Insert the HTML content into the placeholder element
           $('#load-media').html(data);
        })
        .catch(error => console.error('Error loading HTML snippet:', error));
    fetch('/template/seo.html')
        .then(response => response.text())
        .then(data => {
            // Insert the HTML content into the placeholder element
           $('#load-seo').html(data);
        })
        .catch(error => console.error('Error loading HTML snippet:', error));
    fetch('/template/publish.html')
        .then(response => response.text())
        .then(data => {
            // Insert the HTML content into the placeholder element
            $('#load-publish').html(data);
        })
        .catch(error => console.error('Error loading HTML snippet:', error));
})