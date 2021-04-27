function useTheForce () {
    radio.sendString(force)
}
input.onGesture(Gesture.TiltLeft, function () {
    force = "drop"
    useTheForce()
})
input.onGesture(Gesture.TiltRight, function () {
    force = "lift"
    useTheForce()
})
let force = ""
radio.setGroup(1)
