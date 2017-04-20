var CACHE_NAME = 'dcatcher-phrasebook-cache-v1';
var urlsToCache = [
  '/phrasebook',
  '/static/css/main.css',
  '/static/js'
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});