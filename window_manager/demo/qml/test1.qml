import QtQuick 2.5
import QtQuick.Controls 1.4


Rectangle{
    id: rect
    color: "red"

    width: 300;height: 300

    signal crateYellow()
    signal closeWindow()

    Row{
        id: btnRow
        anchors.centerIn: parent
        spacing: 30
        Text {
            id: createLabel
            text: qsTr("创建黄色窗口")
            font.pixelSize: 16
            color: "gray"
            MouseArea{
                anchors.fill: parent
                hoverEnabled: true
                onEntered: parent.color = "white"
                onExited: parent.color="gray"
                onClicked: crateYellow()
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

    TextField{
        id: field
        width: 200
        height: 30
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: btnRow.bottom
        anchors.topMargin: 40
//        inputMethodHints: Qt.ImhSensitiveData
//        inputMethodHints: Qt.ImhHiddenText
        Keys.onPressed: {
            if(event.key == Qt.Key_Control){
                console.log("pressed Ctrl")
                updateInput()
            }
        }
    }

    function updateInput(){
        var win = Qt.createQmlObject("import QtQuick.Window 2.2;Window{color:\"transparent\";flags:Qt.FramelessWindowHint}",rect)
        win.show()
        win.destroy()
    }
}
