(function(){
  function track(method,el){try{if(window.gtag)gtag('event','share',{method:method,content_type:'blog_post',item_id:el.dataset.slug||location.pathname});}catch(e){}}
  document.querySelectorAll('.share').forEach(function(bar){
    bar.querySelectorAll('a[data-method]').forEach(function(a){a.addEventListener('click',function(){track(a.dataset.method,bar);});});
    var copy=bar.querySelector('[data-copy]');
    if(copy){copy.addEventListener('click',function(){
      var u=bar.dataset.url,done=function(){copy.textContent='Copied';setTimeout(function(){copy.textContent='Copy link';},1800);};
      track('copy_link',bar);
      if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(u).then(done,function(){window.prompt('Copy this link',u);});}
      else{window.prompt('Copy this link',u);}
    });}
    var nat=bar.querySelector('[data-native]');
    if(nat&&navigator.share){nat.hidden=false;nat.addEventListener('click',function(){track('native',bar);navigator.share({title:bar.dataset.title,url:bar.dataset.url}).catch(function(){});});}
  });
})();
