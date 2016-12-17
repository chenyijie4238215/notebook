import QtQuick 2.5
import QtQuick.Controls 1.4

Loader{
    id: stackView
    width: 300
    height: 300
//    initialItem: yellow
    sourceComponent: yellow

    Component{
        id: yellow
        Page{
            objectName: "yellowPage"
            color: "yellow"
            onNextClicked: {
                stackView.sourceComponent = red
                redPage()
                destruction()
            }
        }
    }

    Component{
        id: red
        Page{
            objectName: "redPage"
            color: "red"
            onNextClicked: {
                stackView.sourceComponent=blue
                bluePage()
            }
            onPreClicked: {
                stackView.sourceComponent = yellow
                yellowPage()
            }
        }
    }

    Component{
        id: blue
        Page{
            objectName: "bluePage"
            color: "blue"
            onPreClicked: {
                stackView.sourceComponent = red
                redPage()
            }
        }
    }

}
