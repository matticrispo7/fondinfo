#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "game.h"
#include <QMainWindow>

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow();
    void new_game(int cols, int rows);

private:
    Game* game_ = nullptr;
};

#endif // MAINWINDOW_H
