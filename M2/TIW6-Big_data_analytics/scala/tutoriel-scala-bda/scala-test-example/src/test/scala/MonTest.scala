


import collection.mutable.Stack
import org.scalatest._

class ExampleSpec extends FlatSpec with Matchers {

  "Function au_cube" should " compute cube of integers" in {
    val x = 5
    Cube.auCube(x) should be (x*x*x)
  }

}

