var tests = tests || {};

tests.assertTrue = function(boolExp, opt_message) {
  if (boolExp) return;
  throw opt_message || 'Failed.';
};
tests.assertIn = function(needle, haystack) {
  tests.assertTrue(haystack.indexOf(needle) >= 0);
};
tests.assertThrows = function(fn, var_args) {
  try {
    fn.apply(Array.prototype.slice.call(arguments, 1));
  } catch (e) {
    return;
  }
  throw 'Failed.';
};
    
tests.testSuite = function(suite) {
  if(typeof suite == 'string') {
    suite = tests[suite].suite;
  }
  angular.forEach(suite, function(test, i) {
    try {
      test();
    } catch (e) {
      console.error('FAILED Test ' + i + ': ' + e);
      return;
    }
    console.info('PASSED Test ' + i);
  });
};