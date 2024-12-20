import logging

from rt_with_exceptions import Runner
import unittest

logging.basicConfig(level=logging.INFO, filemode='w',
                        filename='runner_tests.log', encoding='UTF-8', format="%(levelname)s | %(message)s")

class RunnerTest(unittest.TestCase):

    isFrozen = False

    @unittest.skipIf(isFrozen, "Tests are frozen")
    def test_walk(self):
        try:
            runner = Runner("Petr", speed = -5)
            for i in range(10):
                runner.walk()
            logging.info("'test_walk' выполнен успешно", exc_info=True)
            self.assertEqual(runner.distance, 50)
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(isFrozen, "Tests are frozen")
    def test_run(self):
        try:
            runner = Runner("Petr", "grigoriy")
            for i in range(10):
                runner.run()
            logging.info("'test_run' выполнен успешно'", exc_info=True)
            self.assertEqual(runner.distance, 100)
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(isFrozen, "Tests are frozen")
    def test_challenge(self):
        runner1 = Runner("Petr")
        runner2 = Runner("Petr2")
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()