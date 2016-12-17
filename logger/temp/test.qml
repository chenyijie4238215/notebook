import QtQuick 2.5

Rectangle{
    width: 300
    height: 300
    color: "red"
//    color: "red"
    MouseArea{
        anchors.fill: parent
        onClicked: console.log("测试打印~~~~~~~~~~~~~~~~~~~")
    }
}
