var tests = tests || undefined;
var oth = oth || undefined;
tests.play = {};

tests.play.setup = function() {
  tests.b = new oth.BlackCard('Hello _, foo _?');
  tests.w1 = new oth.WhiteCard('bar');
  tests.w2 = new oth.WhiteCard('baz');
};

tests.play.testInvalid = function() {
  tests.play.setup();
  tests.assertThrows(oth.Play)
  try {
    new oth.Play(tests.b, tests.w1);
  } catch (e) {
    // Good
    return;
  }
  throw 'Failed';
};

tests.play.testValid = function() {
  tests.play.setup();
  new oth.Play(tests.b, tests.w1, tests.w2);
};

tests.play.testRender = function() {
  tests.play.setup();
  var p = new oth.Play(tests.b, tests.w1, tests.w2);
  var result = p.render();
  tests.assertIn(tests.w1.title, result);
  tests.assertIn(tests.w2.title, result);
  var bSub = tests.b.title.split('_')[0];
  tests.assertIn(bSub, result);
};

tests.play.suite = [
    tests.play.testInvalid, tests.play.testValid, tests.play.testRender];
