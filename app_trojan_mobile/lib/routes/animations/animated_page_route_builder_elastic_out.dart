import 'package:flutter/material.dart';

class AnimatedPageRouteBuilderElasticOut extends PageRouteBuilder {
  final Widget route;
  final Duration duration;

  AnimatedPageRouteBuilderElasticOut(
      {required this.route, required this.duration})
      : super(
          transitionDuration: duration,
          reverseTransitionDuration: duration,
          pageBuilder: (BuildContext context, Animation<double> animation,
              Animation<double> secondaryAnimation) {
            return route;
          },
          transitionsBuilder: (BuildContext context,
              Animation<double> animation,
              Animation<double> secondaryAnimation,
              Widget child) {
            animation =
                CurvedAnimation(parent: animation, curve: Curves.elasticOut);
            return ScaleTransition(
                alignment: Alignment.center, scale: animation, child: child);
          },
        );
}
