import QtQuick 2.5
import QtQuick.Controls 1.4

Rectangle{
    id: page
    signal preClicked()
    signal nextClicked()
    signal yellowPage()
    signal redPage()
    signal bluePage()
    signal closeClicked()
    signal move(int offx, int offy)
    signal destruction()

    MouseArea{
        property int startX: 0
        property int startY: 0
        anchors.fill: parent
        onPressed: {
            startX = mouseX
            startY = mouseY
        }

        onPositionChanged: {
            var offx = mouseX - startX
            var offy = mouseY - startY
            move(offx,offy)
        }
    }

    Row{
        anchors.centerIn: parent
        spacing: 30
        Button{
            id: pre
            text: "上一页"
            onClicked: {
                preClicked()
            }
        }
        Button{
            id: next
            text: "下一页"
            onClicked: {
                nextClicked()
            }
        }
        Button{
            id: close
            text: "关闭"
            onClicked: closeClicked()
        }
    }

//    Component.onDestruction: destruction()
}
