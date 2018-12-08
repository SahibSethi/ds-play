var publisherSubscriber = {};

(function(container) {
  var id = 0;

  container.subscribe = function(topic, fn){
    if (!(topic in container)) {
      container[topic] = [];
    }

    container[topic].push({
      'id': ++id,
      'callback': fn
    });

    return id
  }

  container.unsubscribe = function(id) {
    var subscribers = []
    for (var subscriber of container[topic]) {
      if (subscriber.id != id) {
        subscribers.push(subscriber);
      }
      container[topic] = subscribers;
    }
  }

  container.publish = function(topic, data) {
    for (var subscriber of container[topic]) {
      subscriber.callback(data);
    }
  }

})(publisherSubscriber);

var sub1 = publisherSubscriber.subscribe('mouse', function(data) {console.log('sub1', data);});

let promise = new Promise(function(resolve, reject) {
  
});
