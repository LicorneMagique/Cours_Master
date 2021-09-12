class Dog(name:String, breed:String, age:Int, color:String )
{
}

object Main extends App {

  println("ID timestamp, hour, day_of_week, available_bike_stands, available_bikes")
  val bufferedSource = io.Source.fromFile("/home/finalgo/Bureau/main/Cours/Cours_Master/M2/TIW6-Big_data_analytics/scala/tutoriel-scala-bda/data/VeloV.sample.csv")
  println(bufferedSource.codec.name)
  val test = bufferedSource.getLines().toArray
  for (line <- bufferedSource.getLines) {
    val cols = line.split(";")
    println(s"${cols(0)}|${cols(1)}|${cols(2)}|${cols(3)}|${cols(4)}")
  }
  bufferedSource.close

}
