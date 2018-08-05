var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  var myJson = {'name' : 'youjin'}
  res.send(myJson);
});

module.exports = router;
