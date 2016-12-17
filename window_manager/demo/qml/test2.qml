import QtQuick 2.5

Rectangle{
    color: "yellow"

    signal crateRed()
    signal closeWindow()

    width: 300; height: 300

    Row{
        anchors.centerIn: parent
        spacing: 30
        Text {
            id: createLabel
            text: qsTr("创建红色窗口")
            color: "gray"
            font.pixelSize: 16
            MouseArea{
                anchors.fill: parent
                hoverEnabled: true
                onEntered: parent.color = "white"
                onExited: parent.color="gray"
                onClicked: crateRed()
            }
        }

        Text{
            id: closeLabel
            text: "关闭窗口"
            font.pixelSize: 16
            color: "gray"
            MouseArea{
                anchors.fill: parent
                hoverEnabled: true
                onEntered: parent.color = "white"
                onExited: parent.color="gray"
                onClicked: closeWindow()
            }
        }
    }
}
