

const btnTop=document.querySelector(".btntop");
const post = document.getElementById("post_obj");
const likeBtn = document.querySelector('.like-action')
const icon = document.querySelector('.like-action i')
const value = document.querySelector(".ea-1");
const list=document.querySelectorAll(".about-aside-list-item");
const share=document.querySelector(".ea-4")
const links=document.querySelector(".share-toggle")






// Scroll To Top
btnTop.addEventListener("click",function(){
    window.scrollTo({
        top:0,
        left:0,
        behavior:"smooth"
    });
})




// //Share 
// share.addEventListener("click",function(){

//     links.classList.toggle("show-share")

// })


// //update link number 
// likeBtn.addEventListener("click", updateNumberLink)


//get cookie

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');



//create request

function createRequestforLike() {

    let url = '/post/number-of-like';
    var params = { 
    method: 'POST',
    headers: {
        "X-CSRFToken": csrftoken,
        "Accept": "application/json",
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        'post_id':post.value,
    })
    };
    return new Request(url,params);
}


//calculate number of like
function updateNumberLink() {
    
    let request = createRequestforLike()

    fetch(request).then(function(response) {
        return response.json();
    }).then(function(data) {
        if(data['state']==true){
            value.textContent++
            icon.style.color = 'red'
        }else{
            value.textContent--
            icon.style.color = 'rgba(26, 26, 26, 0.4)'
        }
    }).catch(function(ex) {
        console.log("parsing failed", ex);
    });

}






//slide nav-bar

var tablet=window.matchMedia("(max-width:768px)")
var mobile=window.matchMedia("(max-width:480px)")




function openNav(){
    if(tablet.matches){
        document.getElementById("mySidenav").style.width="250px";
        document.body.style.marginLeft="250px"
        document.body.style.height="100%"
        document.body.style.overflow="hidden"
    }
    if(mobile.matches){
        document.getElementById("mySidenav").style.width="150px";
        document.body.style.marginLeft="150px"
        document.body.style.height="100%"
        document.body.style.overflow="hidden"
    }
    
    // window.onscroll = function () { window.scrollTo(0, 0); };

   
    
    
}

function closeNav(){
    document.getElementById("mySidenav").style.width="0px"
    document.body.style.marginLeft="0px"
    document.body.style.height=""
    document.body.style.overflow=""
   

}






const innerUl=document.querySelectorAll(".inner-ul")
const plusBtns=document.querySelectorAll(".plus-btn")





innerUl.forEach((inner)=>{




    
    inner.addEventListener("click",()=>{
        showHidelist= inner.firstElementChild.nextElementSibling
        plusBtn=inner.firstElementChild
        plusBtn.classList.toggle("rotate")
        showHidelist.classList.toggle("show")
        
     
   
        
    })


})
const siteHeader=document.querySelector("#site-header")
const mainPage=document.querySelector(".slide-container")

window.addEventListener("scroll",()=>{
    const scrollHeight=window.pageYOffset;
    const pageHeight=mainPage.getBoundingClientRect().height
  
    
   
    
    if (scrollHeight>=pageHeight){
        document.getElementById("mySidenav").style.width="0px"
        document.body.style.marginLeft="0px"
    }
    


})

const container=document.querySelector("#container")

window.addEventListener("load",()=>{
    container.classList.add("hide-preloader")
})




